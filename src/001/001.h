#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;

class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	unordered_map<int,int> hash_num;
        for (int i= 0; i<nums.size(); ++i) {
        	if (hash_num.count(target - nums[i])) {
        		return {hash_num[target - nums[i]],i};
        	}
        	hash_num[nums[i]]=i;
        }
        return {};
    }
};

