#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

vector<vector<string>> f(){
    unordered_map<string,int> map;
    vector<string> strs={"eat","tea","tan","ate","nat","bat"};
    vector<vector<string>> res;
    if (strs.size()==1 && strs[0]==""){
        return vector<vector<string>>{{""}};
    }
    int loc=0;
    for (int i=0;i<strs.size();i++){
        string s=strs[i];
        sort(s.begin(), s.end());
        if (map.find(s) == map.end()){
            map.insert({s,loc});
            res.push_back(vector<string>{strs[i]});
            loc++;
        }
        else{
            res[map.find(s)->second].push_back(strs[i]);
        }
    }
    for (auto i: res){
        for ( auto a:i){
            cout << a << " ";
        }
        cout << endl;
    }
    return res;
}

int main(){
    f();
}