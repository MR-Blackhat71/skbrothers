check(){
if wget --spider https://raw.githubusercontent.com/pro-hackers/sk-brothers/master/update.v1.1 2>/dev/null; then
cd $HOME/skbrothers/core/src
echo "hai" > update.txt
else
echo
fi
}
check
option(){
if [ -f "$HOME/skbrothers/core/src/update.txt" ];then
cd $HOME/skbrothers/core/src/
bash update.sh
else
echo " "
fi
}
option
banner(){
clear
echo -e '\e[91m
 ██▒   █▓ ▄▄▄       ███▄    █  ██▓  ██████  ██░ ██ 
▓██░   █▒▒████▄     ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒
 ▓██  █▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░
  ▒██ █░░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██ 
   ▒▀█░   ▓█   ▓██▒▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓
   ░ ▐░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
\e[92m   ░ ░░    ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
     ░░    ░   ▒      ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ ░
      ░        ░  ░         ░  ░        ░   ░  ░  ░
     ░                                             '
echo -e "\e[92m                  join us"
echo -e "                 \e[101m:::. All spammer vai brother's .:::\e[0m" 
}
banner

menu(){
echo
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m1\e[92m)\e[0m\e[92m─\e[0m\e[91m Vanish Device\e[0m"
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m2\e[92m)\e[0m\e[92m─\e[0m\e[91m Save Device\e[0m"
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m3\e[92m)\e[0m\e[92m─\e[0m\e[91m Update Vanish\e[0m"
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m4\e[92m)\e[0m\e[92m─\e[0m\e[91m About Coder\e[0m"
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m5\e[92m)\e[0m\e[92m─\e[0m\e[91m Subscribe\e[0m"
echo -e "                 \e[92m─\e[0m\e[92m(\e[91m6\e[92m)\e[0m\e[92m─\e[0m\e[91m Exit\e[0m"
echo
echo -ne "\e[91m─(\e[92m~\e[0m\e[91m)─\e[92mChoose option: \e[0m" 
read option
if [[ $option == 1 || $option == 01 ]]; then
cd $HOME/vanish/core
bash menu.sh
elif [[ $option == 2 || $option == 02 ]]; then
cd $HOME/vanish/core/src/android
bash save.sh
elif [[ $option == 3 || $option == 03 ]]; then
cd $HOME/vanish/core/src
bash update.sh
elif [[ $option == 4 || $option == 04 ]]; then
cd $HOME/vanish/core/src
bash about.sh
elif [[ $option == 5 || $option == 05 ]]; then
clear
am start -a android.intent.action.VIEW -d https://bitly.com/nhytchannel
clear
sleep 3.0
cd $HOME/vanish
bash vanish
elif [[ $option == 6 || $option == 06 ]]; then
clear
echo -e "                    \e[92m Have A Good Day ........! \e[0m"
echo
sleep 3.0
exit 3
else
cd $HOME/vanish
bash vanish
fi
}
$
