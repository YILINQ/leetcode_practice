class Solution {
public:
    int checkMono(int x, vector<int>& arr){
        int result = 0;
        for(int i = 0; i < arr.size(); i++){
            if (arr[i] <= x){
                result ++;
            }
        }
        return result;
    }
    int findDuplicate(vector<int>& nums) {
        int l = 1;
        int r = nums.size() - 1;
        int ans = 0;
        while (l <= r){
            int mid = (l + r) / 2;
            int result = checkMono(mid, nums);
            if (result <= mid){
                l = mid + 1;
            }
            else{
                r = mid - 1;
                ans = mid;
            }
        }
        return ans;
    }
};