import random

print(f"Hi! Ready to lose? (¬‿¬)ツ\n")

while True:
    q_1 = input("Do you want to play? (yes/no): ").upper()

    if q_1 == "YES":
        print("Let's go!\n")
        r_b_s = ["0", "_", ">"]
        g_h= [
            "A toddler could play better! (¬‿¬)ツ\n",
            "Maybe try using brain cells? (⌐■_■)\n",
            "Winning against you is too easy! ヽ(´ー｀)ノ\n"
        ]
        H_haha=["Wow! That was... something! Maybe next time you’ll actually stand a chance! ( ͡° ͜ʖ ͡° )~ \n",
                "Oh dear, was that your best move? Even a turtle would’ve won faster! ¬‿¬\n",
                "YOU WIN! ...this time. (ಠ_ಠ)\n"]

        while True:
            r_c = random.choice(r_b_s)
            hh_G= random.choice(g_h)
            ha_ha=random.choice(H_haha)
            playr_chosis = input("Choose a character (0 =rock) (_ =paper) (> =scissors): ")

            if r_c == "0" and playr_chosis == "_":
                print(f"\n {r_c} vs {playr_chosis} you win \n")
                print(ha_ha)
                break
            elif r_c == "0" and playr_chosis == ">":
                print(f"\n{r_c} vs {playr_chosis}  I win\n")
                print(hh_G)
                break
            elif r_c == "0" and playr_chosis == "0":
                print(f"{r_c} vs {playr_chosis}")
                print("Tie! How boring... Try again! (ー_ー゛)\n")
                continue

            elif r_c == "_" and playr_chosis == "0":
                print(f"\n {r_c} vs {playr_chosis} you win \n")
                print(ha_ha)
                break
            elif r_c == "_" and playr_chosis == ">":
                print(f"\n{r_c} vs {playr_chosis} I win\n")
                print(hh_G)
                break
            elif r_c == "_" and playr_chosis == "_":
                print(f"{r_c} vs {playr_chosis}")
                print("Tie! How boring... Try again! (ー_ー゛)\n")
                continue

            elif r_c == ">" and playr_chosis == "0":
                print(f"\n {r_c} vs {playr_chosis} you win \n")
                print(ha_ha)
                break
            elif r_c == ">" and playr_chosis == "_":
                print(f"\n{r_c} vs {playr_chosis} I win\n")
                print(hh_G)
                break
            elif r_c == ">" and playr_chosis == ">":
                print(f"{r_c} vs {playr_chosis}")
                print("Tie! How boring... Try again! (ー_ー゛)\n")
                continue
            else:
                print("Invalid input. Please choose 0, _, or >.\n")
                break

    elif q_1 == "NO":
        print("Goodbye!\n")
        break

    else:
        print("Please enter 'yes' or 'no'.\n")