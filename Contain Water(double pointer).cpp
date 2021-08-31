#include<iostream>
#include<algorithm>

using namespace std;

class Solution {
public:
    int min(int x, int y){
        if (x <= y){
            return x;
        }
        else{
            return y;
        }
    }
    int maxArea(vector<int>& height) {
        int i = 0;
        int max_area = 0;
        int j = height.size() - 1;
        while(i < j){
            int area = (j - i) * min(height[i], height[j]);
            if (area > max_area){
                max_area = area;
            };
            if (height[i] < height[j]){
                i++;
            }
            else{
                j--;
            }
            // cout << max_area << endl;
        }
        return max_area;
    }
};