echo "Transferring files to /bd-a1/service-result ..."

# TODO: copy output files to directory 
docker cp bd-a1:/home/doc-bd-a1/vis.png service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp bd-a1:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp bd-a1:/home/doc-bd-a1/k.txt service-result/

echo "Transfer Done!"

echo "Stopping container..."
# Close container
docker stop bd-a1
docker rm bd-a1
echo "Container bd-a1 stopped"
