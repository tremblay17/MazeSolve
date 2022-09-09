#include <cmath>
#include <random>
#include <complex>
#include <filesystem>
#include <fstream>
#include <iterator>
#include <memory>
#include <vector>
#include <list>
#include "node.h"
using namespace std;

class HashTable {
    private:
        int x;
    public:
        HashTable(); //Constructor
        ~HashTable(); //Destructor

};

class PriorityQ {
    private:
        int x;
        int y;
        Node first;
        Node last;
    public:
        PriorityQ(); //Constructor
        ~PriorityQ(); //Destructor

        void enqueue();
        void dequeue();
        void maxHeap();
        void minHeap();
        int showMin();
        int showMax();
        void peek();

};

class AStar {
    private:
        int x;
    public:
        AStar(); //Constructor
        ~AStar(); //Destructor
};