#include <stdio.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <w32api/rpc.h>

//Nathaniel Payag

//Turing Machine
//Infinite Tape is a LinkedList
//The Cells that makes the Tape are nodes
//The Header that reads the instruction inside the cell and goes left, right, or stay after reading the instruction is a ...?

typedef struct node {
    struct node* left;
    struct node* right;
    char data;
} node;

node *head = NULL;

typedef struct instruction{
    char WriteVal;
    char MoveDirection;
    int NewState;
}instruction;

node* Node_Add(char data, node *pointer){
    node* NewTemporaryNode = malloc(sizeof(node));
    NewTemporaryNode->data = data;
    //Make a temporary node tracker to keep track because we dont want mess with the head node
    NewTemporaryNode->right = NULL;
    NewTemporaryNode->left = pointer;
    pointer->right = NewTemporaryNode;
    return NewTemporaryNode;
}

void Printing_TheList(){
    node* node = head;
    while(node != NULL){
        printf("%c", node->data);
        node = node->right;
    }
}

int main() {

    //Variables
    char *pInitialTape;
    char initialTape[1000];
    pInitialTape = initialTape;
    //Translates to "The value of the pointerInitialTape is assigned the address of the variable initial tape;

    //int *pNumOfStates;
    int numOfStates;
    //pNumOfStates = &numOfStates;

    //int *pStartState;
    int startState;
    //pStartState = &startState;

    //int *pEndState;
    int endState;
    //pEndState = &endState;

    //Opening the input file
    FILE *file;
    char fileName[1000];
    //Indicate the user of the prompt
    printf("Input File:");
    //Get the user/keyboard output written
    //Type in C:\test.txt when asked
    scanf("%s", &fileName);
    file = fopen(fileName, "r");
    //case 1: no file of such exist
    if (file == NULL) {
        printf("Can't open %s", fileName);
        return 1;
    }

    fscanf(file, "%s %d %d %d", pInitialTape, &numOfStates, &startState, &endState);
    // fscanf(f, "%d", &numStates);
    // fscanf(f, "%d", &startState);
    //fscanf(f, "%d", &endState);
    printf("%s \n", pInitialTape);
    printf("Amount of states: %d \n", numOfStates);
    printf("Starting state: %d \n", startState);
    printf("Ending state: %d \n", endState);

    //Making the head
    head = malloc(sizeof(node));
    head->data = 'A';
    head->left = NULL;
    head->right = NULL;

    node *tracker = head;

    for (int x = 0; x < strlen(pInitialTape); x++) {
        tracker = Node_Add(pInitialTape[x],tracker);
    }
    printf("Initial Tape Content:");
    Printing_TheList();
    tracker = head;

    //Read the rest of the file, essentially which holds the instructions
    instruction InstructionIn2D [numOfStates][128];
    //128 because we will take the ascii value of the data(char)

    //declaring the variables of the instruction given in the file
    int CurrentState;
    char readValue;

    char writeValue;
    char moveDirection;
    int NewState;

    char *line = NULL;
    size_t len = 0;
    ssize_t fRead;
    while ((fRead = getline(&line, &len, file)) != -1){
        sscanf(line, "(%d,%c)->(%c,%c,%d)", &CurrentState, &readValue, &writeValue, &moveDirection, &NewState);
        // read the rest of file, get the instructions, and store it in the aarray
        instruction temporarystructinstrution;

        //put the value that was just read into the instruction and then put the instruction into the 2d Array
        temporarystructinstrution.WriteVal = writeValue;
        temporarystructinstrution.MoveDirection = moveDirection;
        temporarystructinstrution.NewState = NewState;

        InstructionIn2D[CurrentState][(int) readValue] = temporarystructinstrution;
    }

    //Performing the instruction given
    CurrentState = startState;
    node *tempnode = head;
    int z;
    while(CurrentState != endState){
        z = (int)tempnode->data;

        tempnode->data = InstructionIn2D[CurrentState][(int)z].WriteVal;
        //next
        //if in the given instruction the direction says 'Right'
        if(InstructionIn2D[CurrentState][z].MoveDirection == 'R'){
            if(tempnode->right == NULL){
                tracker = Node_Add('B', tracker);
                tempnode = tempnode->right;
            } else {
                tempnode = tempnode->right;
                tracker = tracker->right;
            }
            //Done with the right side
        } else {
            if(tempnode->left == NULL){
                tempnode = head;
                tracker = head;
            } else {
                tempnode = tempnode->left;
                tracker = tracker->left;
            }
        }
        CurrentState = InstructionIn2D[CurrentState][z].NewState;
    }
    printf("\n");
    Printing_TheList();

    return 0;
}
//Creating the Two Dimensional Array ~~~HALLE help
//    instruction **instructionArr = (struct Instruction **) malloc(numOfStates * sizeof(struct instruction *));
//    for (int n = 0; n < numOfStates; n++) {
//        instructionArr[n] = (struct Instruction *) malloc(128 * sizeof(struct instruction));
//    }
//