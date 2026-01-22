#include<iostream>
#include<cmath>
using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int sum=0;
        for(unsigned short  i=0; short (i<s.size()-1);i++){
            sum+=abs(s[i]-s[i+1]);
            cout << sum<<endl;
        }
        return sum;
    }
};

int main(){
    Solution s;
    s.scoreOfString("asd");
}