        				                	 **ZEVA Syntax**

Basic Types (numbers, booleans, strings):    

	Declaration format: var <type> 
	
	var <type>  x= <data>; @ we have to always end a statement with a semicolon(;)
	
	<type> :=int @integer (1,2)
	
	|str @string (“compiler”)
	
	|bool @boolean (true,false)
	
	var str s;
	
	s[i, i+5] for string slicing 
	
	var str c;

	s.con(c); @for concatenating two strings we have to give as string_1.con(string2)

	zout (x);	 @prints x;

unary-operator ::= 

		   ++ @increment by 1
                   | — @ decrement by 1

binary-operator ::= 	
			
   			+ @addition
		        | - @subtraction	  
		        | * @multiplication
		        | / @division
		        | % @remainder
	  		| @ power
		        |== @comparision of identifier with the required  value
		        |<  @less than symbol
		        |>  @greater than symbol
		        |<= @less than equal symbol
	                |>= @greater than symbol
		        |!= @not equal

@ single line comment @
Identifiers: alphanumeric
             
Compound Types :

              tuple  <Identifier>=(data); @they are immutable
		
  	      array  <Identifier>< <type> > = {data}; @same data type elements are only stored
	 
              list <Identifier>=[];      @ all the three have 0 based indexing
!!!
             For both list and array same basic operations are applied
	     
             <Identifier>.add(data); @adds data to the compound type
	     
             <Identifier>.delete(); @removes the last data of the compound type
	     
             size=<Identifier>.size();
	     
             var <type>a=<identifier>[1]; @ for accessing the second element in the array or tuple here type is the type
	     
             <Identifier>.front(); @ gives the first element of the compound type
	     
             <Identifier>.rear(); @giving the last element of the compound type
	     
!!!
          
Conditionals :

            if (@condition)
            begin
                 @code
            end
            elif(@condition)
            begin
                 @code
            end
            else
            begin
                 @code
            end
	    
@nested if statements

            if(@condition) 
            begin
                 @code 
                  if(@condition2)
                  begin
                        @code
                   end
                 elif(@condition)
            begin
                 @code
            end
            else
            begin
                 @code
            end

        end

Loops : 

           while(condition)
          begin
                 @code
            end
	    
  @ we can also use nested loops
  
         while(condition)
          begin
                 @code
                  while(condition)
                  begin
                         @code
                  end

          end
	  

	     
Functions : 
           
	   return; @ returns the element given there
           func myfunction(arguments) @example myfunction(int x,int y)
           begin
                 @function body
             return data;
            end
            myfunction(x,y); @ for calling function again anywhere after the function declaration


Closures : 

             func myfunction(int x,int y)
             begin 
                   var x=5;
                   var y= 6;
                   func myFunction(int a)
                   begin
                         var a=7;
                        @function body
                        var int output=x=y+a;
                        return output;
                   end
                   return myFunction;
              end
	      
Mutable variables : 

             var <type> | lists @ these are mutable variables
	     
Exceptions : 

             try
               begin
                 @ try the case 
                 @if fails throw the exception
               end
              except(exception)
               begin
                   @do the code given here
               end
             


