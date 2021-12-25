class Solution {
    public int findKthPositive(int[] arr, int k) {
        int left=0;
        int right=arr.length;
        int m;
        while(left < right){
            m=(left+right)/2;
            if(arr[m]-m-1<k){left=m+1;}
            else{right=m;}
        }
        return left+k;
    }
}