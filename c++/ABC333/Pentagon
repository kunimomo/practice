#include <bits/stdc++.h>
using namespace std;

int checkLength(string A);

int main() {
  string S,T;
  cin >> S;
  cin >> T;
  
  if (checkLength(S) == checkLength(T)) {
    cout << "Yes";
  } else {
    cout << "No";
  }
  
  return 0;
}

int checkLength(string A) {
  if (A == "AB" || A == "BA" || A == "BC" || A == "CB" || A == "CD" || 
        A == "DC" || A == "DE" || A == "ED" || A == "AE" || A == "EA") {
        return 1;
    } else if (A == "AC" || A == "CA" || A == "BD" || A == "DB" || A == "CE" || 
               A == "EC" || A == "AD" || A == "DA") {
        return 2;
    } else {
        return 0;
    }
}
