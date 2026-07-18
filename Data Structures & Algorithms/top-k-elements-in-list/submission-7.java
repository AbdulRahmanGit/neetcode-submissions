class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        for (int num:nums){
            count.put(num, count.getOrDefault(num,0) + 1);

        }
        PriorityQueue<int[]> arr = new PriorityQueue<>((a,b)-> a[0] - b[0]);
        for (Map.Entry<Integer,Integer> entry:count.entrySet()){
            arr.offer(new int[] {entry.getValue(), entry.getKey()});
if (arr.size() > k){
    arr.poll();
}
        }
        
        int[] res = new int[k];
        for (int i = 0; i < k; i++){
            res[i] = arr.poll()[1];
        }
        return res;
    }
}
