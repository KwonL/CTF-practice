# Roulette

There is one bug at line num 194. 

```
bet = get_bet();

long get_bet() {
  while(1) {
    puts("How much will you wager?");
    printf("Current Balance: $%lu \t Current Wins: %lu\n", cash, wins); 
    long bet = get_long(); 
    if(bet <= cash) {
      return bet;
    } else {
      puts("You can't bet more than you have!");
    }
  }
}
```

as you can see, get_bet function return unsigned long, but bet's actual type is signed long. So, we can use some negative number (ex: 2158743023)

Then,,We have to win at least 3 times. And there is some vulnerability in rand() function. If we can know seed, we can know what value rand function will generate. Fortunately, seed is our initial cash!

So I made easy emulator for rand function. win 3 times,, get flag.

`picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_25142e09}`