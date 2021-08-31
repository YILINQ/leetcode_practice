#include<iostream>
class Solution {
public:
    int min(int x, int y){
        if (x < y){
            return x;
        }
        else{
            return y;
        }
    }
    int calculate_water(int i, int j, vector<int>& height){
        int total = 0;
        int bar = min(height[i], height[j]);
        for(int t = i; t < j; t++){
            if (bar - height[t] >= 0){
                total += bar - height[t];
            }
        }
        return total;
    }
    int trap(vector<int>& height) {
        vector<int> left;
        vector<int> right;
        int total = 0;
        left.resize(height.size());
        right.resize(height.size());

        int max_left = height[0];
        int max_right = height[height.size() - 1];
        for(int i = 0; i < height.size(); i++){
            left[i] = max_left;
            if(height[i] > max_left){
                max_left = height[i];
            }
        }
        for(int i = right.size()-1; i >=0; i--){
            right[i] = max_right;
            if(height[i] > max_right){
                max_right = height[i];
            }
        }
        for(int i = 0; i < height.size(); i++){
            if (this->min(left[i], right[i]) > height[i]){
                total += min(left[i], right[i]) - height[i];
            }
        }




        return total;
    }
};