class Solution {
    public String longestCommonPrefix(String[] strs) {
    //     String prefix = strs[0];

    //     for(int i = 1; i < strs.length;i++){
    //         int j = 0;
    //         while (j < Math.min(prefix.length(), strs[i].length())){
    //             if (prefix.charAt(j) != strs[i].charAt(j)){
    //                 break;

    //             }
    //             j++;


    //         }
    //         prefix = prefix.substring(0,j);
    //     }
    // return prefix;
    StringBuilder res = new StringBuilder();
    for (int i = 0; i < strs[0].length(); i++){
        for (String s : strs){
            if( i == s.length() || s.charAt(i) != strs[0].charAt(i)){
                return res.toString();
            }
        }
        res = res.append(strs[0].charAt(i));
    }
    return res.toString();

    }
}