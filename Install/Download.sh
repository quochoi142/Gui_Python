sudo -u $USER unzip $HATCHING/resources_tmp.zip -d $HATCHING/resources
sudo -u $USER unzip $HATCHING/resources_tmp2.zip -d $HATCHING/resources
sudo -u $USER mv $HATCHING/resources/resource_2/* $HATCHING/resources/
sudo -u $USER unzip $HATCHING/Resource_for_1st_integration.zip -d $HATCHING/resources
sudo -u $USER mv $HATCHING/resources/Resource_for_1st_integration/* $HATCHING/resources/
sudo -u $USER unzip $HATCHING/resources/Office.zip -d $HATCHING/resources