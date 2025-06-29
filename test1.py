import pygame
from pygame.locals import *
from enum import Enum

# 初始化Pygame
pygame.init()
pygame.mixer.init()

# 全局常量
SCREEN_SIZE = (800, 600)
FPS = 60


# 游戏状态枚举
class AppState(Enum):
    MAIN_MENU = 0
    PLAYING_GAME1 = 1
    PLAYING_GAME2 = 2
    SETTINGS = 3


# 游戏管理器基类
class BaseGame:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def exit(self):
        self.running = False


# ======== 闯关游戏实现 ========
class PlatformGame(BaseGame):
    def __init__(self, screen):
        super().__init__(screen)
        self.player = pygame.Rect(100, 100, 30, 50)
        self.platforms = [pygame.Rect(0, 550, 800, 50)]
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_force = -15

    def handle_events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE and self.velocity.y == 0:
                self.velocity.y = self.jump_force

    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = (keys[K_RIGHT] - keys[K_LEFT]) * 5
        self.velocity.y += self.gravity

        # X轴移动
        self.player.x += self.velocity.x
        for plat in self.platforms:
            if self.player.colliderect(plat):
                if self.velocity.x > 0:
                    self.player.right = plat.left
                elif self.velocity.x < 0:
                    self.player.left = plat.right

        # Y轴移动
        self.player.y += self.velocity.y
        for plat in self.platforms:
            if self.player.colliderect(plat):
                if self.velocity.y > 0:
                    self.player.bottom = plat.top
                    self.velocity.y = 0
                elif self.velocity.y < 0:
                    self.player.top = plat.bottom
                    self.velocity.y = 0

    def draw(self):
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)
        for plat in self.platforms:
            pygame.draw.rect(self.screen, (100, 200, 100), plat)


# ======== 棋牌游戏实现 ========
class CardGame(BaseGame):
    def __init__(self, screen):
        super().__init__(screen)
        self.cards = [
            pygame.Rect(100 + i * 120, 300, 100, 140)
            for i in range(5)
        ]
        self.selected_card = -1

    def handle_events(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for i, card in enumerate(self.cards):
                if card.collidepoint(event.pos):
                    self.selected_card = i

    def update(self):
        pass

    def draw(self):
        self.screen.fill((50, 50, 150))
        for i, card in enumerate(self.cards):
            color = (200, 200, 0) if i == self.selected_card else (255, 255, 255)
            pygame.draw.rect(self.screen, color, card)
            pygame.draw.rect(self.screen, (0, 0, 0), card, 2)


# ======== 主应用程序 ========
class GameApp:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.state = AppState.MAIN_MENU
        self.current_game = None
        self.volume = 0.5

        # 菜单配置
        self.menu_items = {
            AppState.MAIN_MENU: [
                ("开始闯关游戏", AppState.PLAYING_GAME1),
                ("开始棋牌游戏", AppState.PLAYING_GAME2),
                ("游戏设置", AppState.SETTINGS),
                ("退出游戏", "exit")
            ],
            AppState.SETTINGS: [
                ("音量 +", "vol_up"),
                ("音量 -", "vol_down"),
                ("返回主菜单", AppState.MAIN_MENU)
            ]
        }
        self.selected_index = 0
        self.font = pygame.font.Font(None, 40)

    def run(self):
        running = True
        while running:
            # 事件处理
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if self.state == AppState.MAIN_MENU or self.state == AppState.SETTINGS:
                    self.handle_menu_events(event)
                elif self.current_game:
                    self.current_game.handle_events(event)

            # 状态更新
            if self.current_game:
                self.current_game.update()

            # 画面绘制
            if self.state in [AppState.MAIN_MENU, AppState.SETTINGS]:
                self.draw_menu()
            elif self.current_game:
                self.current_game.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_menu_events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.menu_items[self.state])
            elif event.key == K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.menu_items[self.state])
            elif event.key == K_RETURN:
                self.handle_menu_selection()

    def handle_menu_selection(self):
        current_menu = self.menu_items[self.state]
        item = current_menu[self.selected_index][1]

        if isinstance(item, AppState):
            if item == AppState.PLAYING_GAME1:
                self.current_game = PlatformGame(self.screen)
            elif item == AppState.PLAYING_GAME2:
                self.current_game = CardGame(self.screen)
            self.state = item
        elif item == "exit":
            pygame.quit()
            exit()
        elif item == "vol_up":
            self.volume = min(1.0, self.volume + 0.1)
        elif item == "vol_down":
            self.volume = max(0.0, self.volume - 0.1)

    def draw_menu(self):
        self.screen.fill((0, 0, 50))
        menu_title = "主菜单" if self.state == AppState.MAIN_MENU else "设置"
        title_surf = self.font.render(menu_title, True, (255, 255, 255))
        self.screen.blit(title_surf, (350, 100))

        for i, (text, _) in enumerate(self.menu_items[self.state]):
            color = (255, 0, 0) if i == self.selected_index else (255, 255, 255)
            text_surf = self.font.render(text, True, color)
            self.screen.blit(text_surf, (300, 200 + i * 60))

        # 显示音量
        if self.state == AppState.SETTINGS:
            vol_text = f"当前音量: {int(self.volume * 100)}%"
            vol_surf = self.font.render(vol_text, True, (200, 200, 0))
            self.screen.blit(vol_surf, (300, 400))


if __name__ == "__main__":
    app = GameApp()
    app.run()