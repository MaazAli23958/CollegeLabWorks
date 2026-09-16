#include <stdio.h>
#include <stdint.h>

void printIP(uint32_t ip){
    printf("%u.%u.%u.%u",
    (ip >> 24) & 255,
    (ip >> 16) & 255,
    (ip >> 8) & 255,
    
	(ip & 255)
	);
}

int main() {
    unsigned int a, b, c, d;
    unsigned int m1, m2, m3, m4;
    uint32_t ip, mask, network, broadcast;
    uint32_t firstHost, lastHost;
    int prefix = 0;
    int i;
    printf("Enter IPv4 address: ");
    scanf("%u.%u.%u.%u", &a, &b, &c, &d);
    printf("Enter Subnet Mask: ");
    scanf("%u.%u.%u.%u", &m1, &m2, &m3, &m4);

    ip = ((uint32_t)a << 24) |
        ((uint32_t)b << 16) |
        ((uint32_t)c << 8) | d;

    mask = ((uint32_t)m1 << 24) |
        ((uint32_t)m2 << 16) |
        ((uint32_t)m3 << 8) | m4;

    network = ip & mask;
    broadcast = network | (-mask);

    for(i = 32; i >= 0; i--){
        if((mask >> i) & 1)
            prefix++;
        else
            break;
    }
    if(mask == 0xFFFFFFFF){
        firstHost = network;
        lastHost = broadcast;
    }
    else{
        firstHost = network +1;
        lastHost = broadcast -1;
    }
    printf("\n--- Network Information ---\n");

    printf("Network ID  : ");
    printIP(network);

    printf("\nBroadcast Address: ");
    printIP(broadcast);

    printf("\nFirst Host    : ");
    printIP(firstHost);

    printf("\nLast Host     : ");
    printIP(lastHost);

    printf("CIDR Notation      : ");
    printIP(ip);
    printf("%d", prefix);

    if(prefix >= 31)
        printf("\nValid Hosts   : 0");
    else
        printf("\nValid Hosts   : &llu", (1ULL << (32 - prefix)) - 2);

    printf("\nIP Address Class : ");
    if(a >= 1 && a <= 126)
        printf("A");
    else if(a >= 128 && a <= 191)
        printf("B");
    else if(a >= 192 && a <= 223)
        printf("C");
    else if(a >= 224 && a <= 239)
        printf("D");
    else if(a >= 240 && a <= 255)
        printf("E");
    else    
        printf("Invalid");
    printf("\n");

    return 0;
}
