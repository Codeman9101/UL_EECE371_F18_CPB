void printArray (const int [][2]);
const int r1 = 2;
const int cr = 2;
const int c2 = 2;
int A[r1][cr] = {1, 2, 3, 4};
int B[cr][c2] = {1, 2, 3, 4};
int C[r1][c2] = {0, 0, 0, 0};
void setup() {
Serial.begin(9600);

}

void loop() {
  Serial.println("\r");
  printArray(A);
  Serial.println("\r");
  printArray(B);


  for (int i = 0; i < r1; i++) {
    for (int j = 0; j < cr; j++) {
      C[i][j] = 0;
      for (int k = 0; k < cr; k++) {
        C[i][j] = C[i][j] + A[i][k] * B[k][j];
      }
    }

  }
  Serial.println("\r");
  printArray(C);
  delay(10000000);
}
void printArray( const int a[][ c2 ] ) {
  // loop through array's rows
  for ( int i = 0; i < r1; ++i ) {
    // loop through columns of current row
    for ( int j = 0; j < c2; ++j ){
      Serial.print (a[ i ][ j ] );
      Serial.print(" ");
    }
    Serial.println ("\r") ; // start new line of output
  }
}
