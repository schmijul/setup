interface=1
mac=$2


echo " flushing up addr"
echo " "
sudo ip addr flush dev $interface

echo " setting ip link down"

echo " "
echo " "
echo "assinging new mac address"
echo " "

sudo ip link set dev $interface addres $mac

echo " setting ip link up"
echo " "
echo " "
echo " dhclient"

sudo dhcslient -v $interface
