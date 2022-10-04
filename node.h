#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    int x;
    int y;
    int p;
    Node* next;
  
    // Default constructor
    Node(): x(0), y(0), p(0), next(nullptr) {}
  
    // Parameterised Constructor
    Node(int x, int y, int p): x(x), y(y), p(p), next(nullptr) {}
    Node(int x, int y, int p, Node* next): x(x), y(y), p(p), next(next) {}

};