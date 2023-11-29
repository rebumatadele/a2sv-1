class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int length=INT_MAX;
        int start=0;
        int end=0;
        int current_sum=0;
        for(end=0; end<nums.size(); end++){
            current_sum +=nums[end];
            while(current_sum>=target){
                length = min(length, end-start+ 1);
                current_sum -=nums[start];
                start++;
            }
        }
        
        
        return (length !=INT_MAX) ? length: 0;
    }

};