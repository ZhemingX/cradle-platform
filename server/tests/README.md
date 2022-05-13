# Server Unit Tests

This directory contains unit tests for the server as opposed to `server/systemTests` 
which contains system (aka integration) tests. Unit tests run in isolation without any
database. Tests in this directory should test server logic using mocks whenever needed.

Tests which utilize the server's REST API or which require a backing database with 
predefined test data should be placed in the [`server/systemTests`](../systemTests) 
directory.
