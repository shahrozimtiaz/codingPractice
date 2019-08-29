#include <iostream>
using namespace std;

string longestSub(string s1,string s2){
	string temp = "";
	string answer = "";
	string shortest = "";
	for(int i=0;i<s1.length();i++){
		temp=s2;
		for(int j=i;j<s1.length();j++){
			char ch = s1[j];
			if(temp.find(ch) !=-1){
				answer+=ch;
				temp=temp.substr(temp.find(ch)+1);
			}
		}
		if(answer.length()>shortest.length())
			shortest = answer;
		answer="";
	}
	return shortest;
}
int main(){
	string s1,s2;
	cin >> s1;
	cin >> s2;

	string answer = longestSub(s1,s2);
	cout<<"Final: "<<answer<<endl;
}