#include <stdio.h>;

unsigned int is_match(char* buf){

    long long a = 0xCBF29CE484222325;
    long long b = 0x6465C067C31FE99E;
    // long long b = 0x270163F106DBE9DD;
    long long c = 0x100000001B3;

    long long checksum = a;
    for (int i = 0; i < 27; i++){
        long long _ = (long long)buf[i];
        checksum = checksum ^ _;
        checksum = checksum * c;
    }

    if (checksum == b)
        return 1;
    return 0;
}

int main(){
    
    char buf[28] = "1357SearchG00gleaaaaaaM3m3s";

    char chars[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

    long long counter = 0;


    // for (int i_1 = 0; i_1 < 62; i_1++){
    //     for (int i_2 = 0; i_2 < 62; i_2++){
    //         for (int i_3 = 0; i_3 < 62; i_3++){
    //             for (int i_4 = 0; i_4 < 62; i_4++){
                   
    //                 buf[0] = chars[i_1];
    //                 buf[1] = chars[i_2];
    //                 buf[2] = chars[i_3];
    //                 buf[3] = chars[i_4];
    //                 buf[4] = '\0';
                    

    //                 if (is_match(buf) != 0){
    //                     printf("%s\n",buf);
    //                     exit(0);
    //                 }

    //                 counter++;
    //                 if (counter % 1000000 == 0){
    //                     printf("%ll\n",counter);
    //                 }
    //             }
    //         }
    //     }
    // }

    for (int i_1 = 0; i_1 < 62; i_1++){
        for (int i_2 = 0; i_2 < 62; i_2++){
            for (int i_3 = 0; i_3 < 62; i_3++){
                for (int i_4 = 0; i_4 < 62; i_4++){
                    for (int i_5 = 0; i_5 < 62; i_5++){
                        for (int i_6 = 0; i_6 < 62; i_6++){
                            buf[16] = chars[i_1];
                            buf[17] = chars[i_2];
                            buf[18] = chars[i_3];
                            buf[19] = chars[i_4];
                            buf[20] = chars[i_5];
                            buf[21] = chars[i_6];
                            

                            if (is_match(buf) != 0){
                                printf("%s\n",buf);
                                exit(0);
                            }

                            counter++;
                            if (counter % 10000000 == 0){
                                printf("%llu -> %s\n",counter, buf);
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}