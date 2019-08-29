#include <iostream>
#include <vector>
using namespace std;

vector<string> checkBalance(vector<string> vec1){
  vector<string> answer;
  bool ans = true;
  for(int s=0;s<vec1.size();s++){
    string str1 = vec1[s];
    if(str1.length()==0){
      answer.push_back("String is empty..");
    }
    else if(str1.length()%2==1){
      answer.push_back("No");
    }
    else{
      for(int i=0;i<str1.length()-1;i++){
	if(str1.at(i) == '(' && str1.at(i+1) != ')'){
	  ans = false;
	  break;
	}
	if(str1.at(i) == '{' && str1.at(i+1) != '}'){
	  ans = false;
	  break;
	}
	if(str1.at(i) == '[' && str1.at(i+1) != ']'){
	  ans = false;
	  break;
	}
      }
      if(ans){answer.push_back("Yes");}
      else{answer.push_back("No");}
    }
  }
  return answer;
}

int main(){
  vector<string> vec;
  string s0 = "";
  string s1 = "{";
  string s2 = "{}[]()";
  string s3 = "[{]}()";
  string s4 = "{}[}()";

  vec.push_back(s0);
  vec.push_back(s1);
  vec.push_back(s2);
  vec.push_back(s3);
  vec.push_back(s4);
  
  vector<string> answer1 = checkBalance(vec);

  for(int i=0;i<answer1.size();i++)
  cout<<i+1<<": "<<answer1[i]<<endl;
}