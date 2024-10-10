class NimPlayer:
  def __init__(self):
    self.board = []
  
  def play(self, boardState):
    self.board = boardState
    newBoardState = self.move(boardState)
    self.board = newBoardState
    print("Start of turn board state: ", boardState, "  |  End of turn board state: ", newBoardState)
    return newBoardState




  def move(self, board):
    # Calculate every board position
    possibleStates = []
    for i in range(len(board)): 
        # For each row of the nim board, find every possible number of sticks to remove
        for sticks_to_remove in range(1, board[i]+1):
            # Create a new list representing the new potential board state
            potentialState = board.copy()
            potentialState[i] -= sticks_to_remove
            possibleStates.append(potentialState.copy())
    
    # Prioritize moves that result in a nim sum of 0
    for state in possibleStates:
        if self.nimSum(state) == 0:
            print("Found sum zero state to return to opponent: ", state)
            return state

    # If no nim sum 0, return the first valid state that isn't a loss
    for state in possibleStates:
        if sum(state) != 0:
            return state

    # If no non-zero sum state is found, return the first state
    return possibleStates[0]
    
      

  def nimSum(self, board):
      # Initialize nim_sum to 0
      nim_sum = 0
      # Perform XOR for each pile one by one
      for pile in board:
          # Perform the bitwise XOR operation
          nim_sum = nim_sum ^ pile  
      return nim_sum