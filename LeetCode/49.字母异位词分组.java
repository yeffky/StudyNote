/*
 * @Author: yeffky
 * @Date: 2025-06-10 10:39:43
 * @LastEditTime: 2025-06-11 09:59:20
 */
/*
 * @lc app=leetcode.cn id=49 lang=java
 *
 * [49] 字母异位词分组
 */

// @lc code=start

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<Integer>> map = new HashMap();
        for (String str : strs) {
            String[] strArray = str.split("");
            Arrays.sort(strArray);
            StringBuilder stringBuilder = new StringBuilder();
            for (String letter : strArray) {
                stringBuilder.append(letter);
            }
            String newStr = stringBuilder.toString();
            if (!map.containsKey(newStr)) {
                ArrayList list = new ArrayList<>();
                list.add(str);
                map.put(newStr, list);
            }
            else {
                ArrayList list = map.get(newStr);
                list.add(str);
            }
        }
        ArrayList ansList = new ArrayList<ArrayList<String>>();
        map.forEach((key, value) -> {
            ansList.add(value);
        }) ;
        return ansList;
    }
}
// @lc code=end
