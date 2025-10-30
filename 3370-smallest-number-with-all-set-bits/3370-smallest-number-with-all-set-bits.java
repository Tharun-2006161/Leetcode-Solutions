class Solution {
    public int smallestNumber(int n) {
        String str1 = "";
        while(n>0){
            str1=Integer.toString(n%2)+str1;
            n=n/2;
        }
        
        int sum=0;
        for(int i=0;i<str1.length();i++){
            sum+=Math.pow(2,i);
        }
        return sum;
    }
}