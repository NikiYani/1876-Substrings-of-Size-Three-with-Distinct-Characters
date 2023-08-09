# 1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters. </br>

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​. </br>

Note that if there are multiple occurrences of the same substring, every occurrence should be counted. </br>

A substring is a contiguous sequence of characters in a string. </br>

## Example 1:

Input: s = "xyzzaz" </br>
Output: 1 </br>
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". </br>
The only good substring of length 3 is "xyz". </br>

## Example 2:

Input: s = "aababcabc" </br>
Output: 4 </br>
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc". </br>
The good substrings are "abc", "bca", "cab", and "abc". </br>

## Constraints:

1 <= s.length <= 100 </br>
s​​​​​​ consists of lowercase English letters. </br>
