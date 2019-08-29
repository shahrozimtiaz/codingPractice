#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	cout<<"Create n digit pin: "<<endl;
	string password = "";
	cin>>password;
	int n = password.length();
	int arr[] = {1,2,3,4,5,6,7,8,9,0};
	vector<int> nums(arr,arr+10); 
	sort(nums.begin(),nums.end());
	string str ="";
	int attempt=0;

	while(next_permutation(nums.begin(),nums.end())){
		for(int i=0;i<nums.size();i++){
			str+=to_string(nums[i]);
		}
		string str2=str.substr(0,n);
		attempt++;
		if(str2==password){
				cout<<endl;
				cout<<"cracked: " + str2<<" in " <<attempt<<" attempts" <<endl;
				break;			}
		str=str2="";
	}
}