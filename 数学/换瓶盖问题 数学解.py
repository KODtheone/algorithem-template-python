'''
 1518. 换水问题   https://leetcode.cn/problems/water-bottles/solutions/339339/huan-jiu-wen-ti-by-leetcode-solution/
你可以用 numExchange 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 numBottles 瓶水。
如果喝掉了水瓶中的水，那么水瓶就会变成空的。
给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。
'''
class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        return (b - e) // (e - 1) + 1 + b if b >= e else b