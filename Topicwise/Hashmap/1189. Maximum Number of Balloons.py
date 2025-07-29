# https://leetcode.com/problems/maximum-number-of-balloons/description/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonDict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in balloonDict:
                balloonDict[char] += 1

        leastChar = min(
            balloonDict["b"],
            balloonDict["a"],
            balloonDict["n"],
            balloonDict["l"] // 2,
            balloonDict["o"] // 2,
        )
        return leastChar


print(Solution().maxNumberOfBalloons("nlaebolko"))
print(Solution().maxNumberOfBalloons("leetcode"))
print(
    Solution().maxNumberOfBalloons(
        "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    )
)
