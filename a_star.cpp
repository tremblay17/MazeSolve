#include "a_star.h"
using namespace std;

PriorityQ_Hash::PriorityQ_Hash()
{
    qHead = nullptr;
    qTail = nullptr;
    q_x = 0;
    q_y = 0;

}


PriorityQ_Hash::~PriorityQ_Hash()
{

}

//Queue Functions

void PriorityQ_Hash::enqueue(int pos_x, int pos_y, int p)
{
    Node* tmp = new Node(pos_x, pos_y, p);
    Node* skip = qHead;
    if(qHead == nullptr){ //insertion into empty list
        qHead = tmp;
        /* qHead->next = qTail;
        qTail->prev = qHead; */
        qTail = qHead;
        delete tmp;
    }
    else if(qHead != nullptr){ //insertion into non-empty list
        if(tmp->p < qHead->p){
            qHead->next = tmp;
            qTail = tmp;
            delete tmp;
        }
        else if(tmp->p < qTail->p){
            qTail->next = tmp;
            qTail = tmp;
            delete tmp;
        }
        else{
            while(skip->next != nullptr){
                skip = skip->next;
                if(tmp->p < skip->p){
                    break;
                }
            }
            tmp->next = skip->next;
            skip->next = tmp;
            skip = qHead;
            tmp = qTail;
            delete skip;
            delete tmp;
        }
    } 
    delete skip;
}

void PriorityQ_Hash::dequeue(int p)
{
    Node* skip = qHead;
    if(p == qHead->p){ //delete head
        qHead = qHead->next;
        delete skip;
    } 
    else if(p == qTail->p){ //delete tail
        while(skip->next != qTail){
            skip = skip->next;
        }
        qTail = skip;
        skip = skip->next;
        delete skip;
    } 
    else { //delete from middle
        Node* tmp;
        while(p != skip->p && (tmp != skip->next)){
            tmp = skip;
            skip = skip->next;
        }
        tmp->next = skip->next;
        tmp = qHead;
        delete skip;
        delete tmp;
}
    }

int PriorityQ_Hash::top()
{
    int x = qHead->x;
    int y = qHead->y;
    int p = qHead->p;
    cout << 'x: %d, y: %d, p: %d' << x, y, p << '\n';
    return (qHead->p);
}

int PriorityQ_Hash::size()
{
    int count = 1;
    Node* skip = qHead;
    while(skip != qTail){
        count += 1;
        skip = skip->next;
    }
    return count;
}

bool PriorityQ_Hash::isEmpty()
{
    if(qHead == nullptr){
        return true;
    }
    else{
        return false;
    }
}

void PriorityQ_Hash::print()
{
    
}

//Hash Table Functions 

void PriorityQ_Hash::search(Node* nodeToSearch)
{

}

void PriorityQ_Hash::delIndex(Node* nodeToDel)
{

}

void PriorityQ_Hash::insert(Node* nodeToIns)
{

}

void PriorityQ_Hash::hashFunc()
{

}


AStar::AStar()
{

}


AStar::~AStar()
{

}


void AStar::AStar1()
{

}

void AStar::AStar2()
{

}

void AStar::AStar3()
{

}
