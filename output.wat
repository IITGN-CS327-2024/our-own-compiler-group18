(module
  (func $caesarEncrypt (param i32 i32 i32) ;; caesarEncrypt(int32 plaintext[], int32 plaintextLength, int32 key)
    local.get 0 ;; Load the address of plaintext array
    local.get 1 ;; Load plaintextLength
    local.get 2 ;; Load key
    i32.const 0 ;; Initialize loop counter
    local.set $i ;; Store loop counter in local variable $i
    (loop
      local.get $i ;; Load loop counter
      local.get 1 ;; Load plaintextLength
      i32.ge_u ;; Check if loop counter >= plaintextLength
      br_if 1 ;; Exit loop if true
      local.get 0 ;; Load address of plaintext array
      local.get $i ;; Load loop counter
      i32.add ;; Add loop counter to the address to get the address of current integer
      i32.load ;; Load the value at the current address
      local.get 2 ;; Load key
      i32.add ;; Add key to the current value
      i32.const 26 ;; Modulus operand
      i32.rem_u ;; Modulus operation with 26
      i32.store ;; Store the result back to the array
      local.get $i ;; Load loop counter
      i32.const 1 ;; Increment loop counter
      i32.add ;; Increment loop counter
      local.set $i ;; Store updated loop counter
      br 0 ;; Continue looping
    )
  )

  (func $caesarDecrypt (param i32 i32 i32) ;; caesarDecrypt(int32 plaintext[], int32 plaintextLength, int32 key)
    local.get 0 ;; Load the address of plaintext array
    local.get 1 ;; Load plaintextLength
    local.get 2 ;; Load key
    i32.const 0 ;; Initialize loop counter
    local.set $i ;; Store loop counter in local variable $i
    (loop
      local.get $i ;; Load loop counter
      local.get 1 ;; Load plaintextLength
      i32.ge_u ;; Check if loop counter >= plaintextLength
      br_if 1 ;; Exit loop if true
      local.get 0 ;; Load address of plaintext array
      local.get $i ;; Load loop counter
      i32.add ;; Add loop counter to the address to get the address of current integer
      i32.load ;; Load the value at the current address
      local.get 2 ;; Load key
      i32.sub ;; Subtract key from the current value
      i32.const 26 ;; Add 26 to ensure positive result
      i32.add ;; Add 26 to ensure positive result
      i32.rem_u ;; Modulus operation with 26
      i32.store ;; Store the result back to the array
      local.get $i ;; Load loop counter
      i32.const 1 ;; Increment loop counter
      i32.add ;; Increment loop counter
      local.set $i ;; Store updated loop counter
      br 0 ;; Continue looping
    )
  )

  (memory (export "memory") 1)
  (export "caesarEncrypt" (func $caesarEncrypt))
  (export "caesarDecrypt" (func $caesarDecrypt))
)
