#!/bin/sh

HATCHING=/home/$USER/.hatch
export PATH=$HATCHING:$PATH


if [ `dpkg-query -l | grep qemu | wc -l` -gt 0 ]
then
    echo "Removing qemu"
    sudo sh -c "apt-get remove --auto-remove qemu" 
    sudo sh -c "apt-get purge --auto-remove qemu"
    sudo sh -c "dpkg --purge  qemu-system-common"
    sudo sh -c "dpkg --purge  qemu-system-x86"
fi

echo "remove qemu-hardened if existing"
if [ `dpkg-query -l | grep qemu-hardened | wc -l` -gt 0 ]
then
    echo "Removing hardened"
    sudo sh -c "sudo -u $USER apt-get remove --auto-remove qemu-hardened"
fi

# install
PKG_LIST=(
    wget
    libyara-dev
    libssh2-1
    libvirglrenderer0    
    p7zip-full
    apparmor-utils
    libbrotli1
    liblz4-tool
    unrar
    unzip
    cabextract
    unace
    daa2iso
    guacd 
    libpq5
    libyara3
    p7zip
    postgresql
    postgresql-10
    postgresql-client-10
    postgresql-client-common
    postgresql-common
    sysstat
    libsnappy-dev
    libaio1
    libaio-dev
    libusbredirparser-dev
    libibverbs-dev
    librdmacm-dev
    libxen-dev
    libfdt-dev
    libspice-server-dev
    libcacard0
    isomd5sum
)

echo "[4/10]. Install nessary package"
for pkg in ${PKG_LIST[@]}
do
    if [ `dpkg-query -l | grep $pkg | wc -l` -eq 0 ]
    then
        echo "install $pkg..."
        sudo sh -c "apt install $pkg -y > /dev/null"
    fi
done

# install libhyperscan5
# https://launchpad.net/ubuntu/+source/hyperscan/5.1.0-1
sudo -u $USER wget -q http://launchpadlibrarian.net/409211617/libhyperscan5_5.1.0-1_amd64.deb
sudo sh -c "dpkg -i libhyperscan5_5.1.0-1_amd64.deb"


echo "Install QEMU Harderning"
sudo sh -c "dpkg -i $HATCHING/qemu-hardened*.deb"

sudo -u $USER mkdir $HATCHING/vmdata
sudo -u $USER mkdir $HATCHING/vmdata/storage
sudo -u $USER mkdir $HATCHING/vmdata/cache
sudo -u $USER mkdir $HATCHING/vmdata/scratch
sudo -u $USER mkdir $HATCHING/vmdata/linux


# if [[ -z "$FILE_PATH" || (! -d "$FILE_PATH") ]]; then
#     # download windows iso
#     echo "[5/10]. download windows iso"
#     echo "download win7 from one driver"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EV0hanqY-FFOg9zAOjiVQWMBWoqXEyJ5zGsOytNGki5smw?download=1 -O $HATCHING/resources/win7ultimate.iso -q --show-progress

#     echo "download win10 from one driver"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/Edr41t0uY7NBpmG5MjzP-ngBn6rMyLm0VGWAUgx3NJiRkA?download=1 -O $HATCHING/resources/Win10_1703_English_x64.iso -q --show-progress

#     echo "download win2016 from one driver"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/ERYd0WjCl49JpiUgyOOSbnYB-2Ow2mqc7Oq0icenM1sM4g?download=1 -O $HATCHING/resources/en_windows_server_2016_x64_dvd_9718492.iso -q --show-progress

#     echo "download office2010 from one driver"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EWKVaiHETXlMkXSXE5BuBtMBhkxfj4wtTTvl2rthvP2wxw?download=1 -O $HATCHING/resources/en_office_professional_plus_2010_x86_x64_dvd_515529.iso -q --show-progress

#     echo "download Ubuntu 1804 base image"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tongqing_liu_opswat_com/EUpS4SnVdtNLvlv8mfxdO60Bnni8OHG7LRzCgmDCG4i_1w?download=1 -O $HATCHING/resources/ubuntu-1804-amd64.qcow2 -q --show-progress

#     echo "download other software files"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/tai_vu_opswat_com/EZYZuDtq8jZAp108Ot3F-HQBNHgP9Op2tauM2BYheQwpXg?download=1 -O $HATCHING/resources_tmp.zip -q --show-progress

#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EbmvfeZp6aRKnXhb1Z00hBUBkGUmwOc-JapMQMYNntQJBQ?download=1 -O $HATCHING/resources_tmp2.zip -q --show-progress

#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EYO8YTWofWhLnKBPDPlhz50BpGmy52ocvYQqXXdRth3eGA?download=1 -O $HATCHING/Resource_for_1st_integration.zip -q --show-progress

#     echo "download CentOS7 minimal"
#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EfCgzTh8OARNvCX1UFE_Y2wBHsJGzi8zHvoUK6icolgetQ?download=1 -O $HATCHING/resources/CentOS-7-x86_64-Minimal-1810.iso -q --show-progress

#     sudo -u $USER wget -q https://opswat2017-my.sharepoint.com/:u:/g/personal/thi_nguyen_opswat_com/EdBqg-HF6ElJqjllW086xVEB0diiooZ8TJ-NPtxWrXcVOA?download=1 -O $HATCHING/resources/Office.zip -q --show-progress

#     # copy other software files to resources folder
#     sudo -u $USER unzip $HATCHING/resources_tmp.zip -d $HATCHING/resources
#     sudo -u $USER unzip $HATCHING/resources_tmp2.zip -d $HATCHING/resources
#     sudo -u $USER mv $HATCHING/resources/resource_2/* $HATCHING/resources/
#     sudo -u $USER unzip $HATCHING/Resource_for_1st_integration.zip -d $HATCHING/resources
#     sudo -u $USER mv $HATCHING/resources/Resource_for_1st_integration/* $HATCHING/resources/
#     sudo -u $USER unzip $HATCHING/resources/Office.zip -d $HATCHING/resources

  
# fi


