 

#include <iostream>
#include <unistd.h>
#include "pseudoDomain.h"

using namespace std;
//using namespace pseudo;

//constructor
pseudoDomain::pseudoDomain()
{
    charge = 100;
    carryingPackage = false;
    gaCount = 10;
    gbCount = 10;
    gcCount = 10;
    dcCount = 5;
}

bool pseudoDomain::not_carrying_packageTP()
{
    return !carryingPackage;
}

bool pseudoDomain::battery_low()
{
    if ( charge < 25) //0.25*charge )
        return true;
    else
        return false;
}

int pseudoDomain::get_charge()
{
    return charge;
}

pseudoDomain::STATUS_FLAG pseudoDomain::GA()
{
    
    charge --;
    if (status_GA != RUNNING)
        gaCount = 10;
    gaCount--;
    if(gaCount > 0)
    {
        cout<<"GA still running\n";
        status_GA = RUNNING;
    }
    else {       
        cout<<"GA returned success and package has now been picked\n\n";
        carryingPackage = true; 
        status_GA = SUCCESS;
    }
    return status_GA;
}

pseudoDomain::STATUS_FLAG pseudoDomain::GB()
{
    charge --;
    if (status_GB != RUNNING)
        gbCount = 10;
    gbCount--;
    if(gbCount > 0)
    {
        cout<<"GB still running\n";
        status_GB = RUNNING;
    }
    else{
        cout<<"GB returned success and the package has now been dropped\n\n";
        carryingPackage = false;
        status_GB = SUCCESS;
    }
    return status_GB;
}


pseudoDomain::STATUS_FLAG pseudoDomain::GC()
{
    gaCount = 5;
    gbCount = 4;
    charge --;
    if (status_GC != RUNNING)
        gcCount = 10;
    gcCount--;
    if(gcCount > 0)
    {
        cout<<"GC still running\n";
        status_GC = RUNNING;
    }
    else
    {
        cout<<"GC returned success and now going to DC\n\n";
        status_GC = SUCCESS;   
    }
    return status_GC;
}

pseudoDomain::STATUS_FLAG pseudoDomain::DC()
{
    
    charge --;
    //sleep(2);
    if (status_DC != RUNNING)
        dcCount = 5;
    dcCount--;
    if(dcCount > 0)
    {
        cout<<"DC still running\n";
        status_DC = RUNNING;
    }
    else
    {
        charge = 100;
        status_DC = SUCCESS;
    }
    return status_DC;
}







