public class Solution {
    public int CountCommas(int n) {
        return CountCommaHelper(n);
    }
    public int CountCommaHelper(int n){
        if (n < 1000)return 0; 
        int commas = (int)(Math.Log10(n)/3);
        int count = n - (int)Math.Pow(1000, commas) + 1;
        return commas * count + CountCommaHelper((int)Math.Pow(1000, commas-1));
    }
}
