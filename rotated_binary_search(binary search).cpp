#include <iostream>

using namespace std;
class Solution {
public:
    int binarySearch(int left, int right, int target, vector<int> &arr){
        if (left > right){
           return -1;
        }
        else{
            int mid = (left + right) / 2;
            if (arr[mid] == target){
                return mid;
            }
            else{
                if (arr[left] <= arr[mid]){
                    if (arr[left] <= target && target <= arr[mid]){
                        return binarySearch(left, mid - 1, target, arr);
                    }
                    else{
                        return binarySearch(mid + 1, right, target, arr);
                    }
                }
                else{
                    if (arr[mid] <= target && target <= arr[right]){
                        return binarySearch(mid + 1, right, target, arr);
                    }
                    else{
                        return binarySearch(left, mid - 1, target, arr);
                    }
                }
            }
        }
    }
    int search(vector<int>& nums, int target) {
        return binarySearch(0, nums.size() - 1, target, nums);

        // v2 = std::vector<int>(v1.begin() + 1, v1.end());
        // vector1.insert( vector1.end(), vector2.begin(), vector2.end() );

    }
};