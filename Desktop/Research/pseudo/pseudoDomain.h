
#ifndef PSEUDO_DOMAIN_H
#define PSEUDO_DOMAIN_H
#include<string>


  class pseudoDomain
  {
      public:
        enum STATUS_FLAG{ RUNNING, SUCCESS, FAILURE} status_GA, status_GB, status_GC, status_DC;
        
        pseudoDomain(); //constructor

        STATUS_FLAG GA();
        STATUS_FLAG GB();
        STATUS_FLAG GC();
        STATUS_FLAG DC();
        bool not_carrying_packageTP();
        bool battery_low();
        int get_charge();
        

      private:
        bool carryingPackage;
        int charge;
        int gaCount, gbCount, gcCount, dcCount;
        
  };




#endif   //PSEUDO_DOMAIN_H






