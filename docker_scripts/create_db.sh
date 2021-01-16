docker run -d --name mongo-test \
 --network first-test --network-alias mongo-test \
 -v test-mongo-data \
 mongo:3.6-xenial