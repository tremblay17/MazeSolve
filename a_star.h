#include <cmath>
#include <random>
#include <complex>
#include <filesystem>
#include <fstream>
#include <iterator>
#include <unordered_map>
#include <array>
#include <list>
#include "node.h"
using namespace std;

class PriorityQ_Hash {
    private:
        int q_x;
        int q_y;
        Node* qHead;
        Node* qTail;

        int numKV; //# of key val pairs
        int size; //size of linear probing table 
        unordered_map<int, vector<int>> keyValPair; //key value table
        void hashFunc();
    public:
        PriorityQ_Hash(); //Constructor
        ~PriorityQ_Hash(); //Destructor

        void enqueue(int pos_x, int pos_y, int p); //inserts node with priority p based on position
        void dequeue(int p); //Finds node with priority p and removes the node
        int top(); //element with highest priority
        int size(); //# of elements
        bool isEmpty(); //checks if empty
        void print(); //prints the queue

        void insert(Node* nodeToIns); //inserts into hash table from q
        void delIndex(Node* nodeToDel); //delete from hash table
        void search(Node* nodeToSearch); //find values in hash table
};

class AStar {
    private:


    public:
        AStar(); //Constructor
        ~AStar(); //Destructor

        void AStar1();
        void AStar2();
        void AStar3();
};