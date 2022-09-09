#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;
  
    // Default constructor
    Node()
    {
        data = 0;
        next = NULL;
        prev = NULL;
    }
  
    // Parameterised Constructor
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
        this->prev = NULL;
    }

    Node(int data, Node* next) {
        this->data = data;
        this->next = next;
        this->prev = NULL;
    }

    Node(int data, Node* next, Node* prev){
        this->data = data;
        this->next = prev;
        this->prev = next;
    }

};