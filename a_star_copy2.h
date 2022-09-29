/*
Code Copied From:
https://github.coventry.ac.uk/jansonsa/D1/tree/master/pokemonGUI/pokemonGUI
*/

#ifndef WORLD_H
#define WORLD_H
#pragma once
#include <iostream>
#include <set>
#include <vector>


using namespace std;

struct Block {
	//Structure for obstacles
	string color;
	int id;

};

inline bool operator < (const Block& lhs, const Block& rhs)
{//We need to overload "<" to put our Block structure into a set
	return lhs.id < rhs.id;
}



class World
{
public:
	World();
	~World();
	World(string name, int id, string pictureLocation, int spawnPoint, vector<World*> exits, char entrance);
	vector<World*> exits;
	char entrance;
	int spawnPoint;
	string pictureLocation;
	string name;
	int id;


	//Used for obstacle recognition and world save/load
	set<Block> blocks;
	string colorName = "black";
	set<int> obstacles;


	//Load and Save functions
	static void saveWorld(std::string fileName);
	static void loadWorld(std::string fileName);

private:

};

extern World world;

#endif