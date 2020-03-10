#include<stdlib.h>
#include<stdio.h>
#include<string.h>

////// structs
struct node 
{ 
    char* data; // string
    struct node* next; // pointer to next
    int count; // MRU counter of occurence
};

struct dict
{
  int size;
  char** list; // store all words
};


struct mru
{
  int size; // from 0 to 10
  struct node* head; // start
  struct node* tail; // end
};
////// structs 


// string sorting
void sortstring(char** str,int n)
{
    int i,j;
    char* temp=(char*)malloc(20*sizeof(char));//20 as word length;

  for(i=0;i<=n;i++)
  {
    for(j=i+1;j<=n;j++)
    {
      if(strcmp(str[i],str[j])>0)
      {
        strcpy(temp,str[i]);
        strcpy(str[i],str[j]);
        strcpy(str[j],temp);
      }
    }
  }
  
  return;
}

// for mru sorting
void mru_sort(char** str,int *a,int n)
{
    int i,j,t;
    char* temp=(char*)malloc(20*sizeof(char));//20 as word length;

  for(i=0;i<=n;i++)
  {
    for(j=i+1;j<=n;j++)
    {
      if(strcmp(str[i],str[j])>0)
      {
        strcpy(temp,str[i]);
        strcpy(str[i],str[j]);
        strcpy(str[j],temp);
        t=a[i];
        a[i]=a[j];
        a[j]=t;
      }
    }
  }
  
  return;
}


// display mru in alphabetical with frequency
void display(struct mru* x)
{
  int n=x->size,i;
  char** c=(char**)malloc(n*sizeof(char*)); // array to store all strings to sort
  for(i=0;i<n;i++)
  {
    c[i]=(char*)malloc(20*sizeof(char));//20 as word length
  }
  int* a=(int*)malloc(n*sizeof(int)); // to sort along with array 
  
  if(x->head == NULL)
  {
    printf("MRU is empty\n");
  }
  struct node* temp=NULL;
  temp=x->head;
  i=0;
  // simply printed insted of sorting
  while(temp!=NULL)
  {
    strcpy(c[i],temp->data);
    a[i]=temp->count;
    temp=temp->next;
    i++;
  }
  
  mru_sort(c,a,n);
  
  
  for(i=0;i<n;i++)
  {
      printf("(%s,%d) ",c[i],a[i]);
  }
  printf("\n");
  return;
}

// increment count of element in mru linked list
void increment(struct node* x)
{
  (x->count)=(x->count)+1;
  return;
}

// is input present in mru  // to_nc specifics if to increment if found
int is_present(struct mru* x,char* s,int to_inc,int to_move)
{

  int flg=0;
  if(x->head == NULL )
  {
    return 0;
  }
  
  struct node* temp=NULL;
  struct node* prev=NULL;
  temp=x->head;
  prev=temp;
  
  while(temp!=NULL)
  {
    if(strcmp(s,temp->data)==0)
    {
      flg=1;
      if(to_inc==1)
      {
        increment(temp);
      }
      if(to_move==1)
      {
        if(prev!=temp)
        {
          prev->next=temp->next;
          temp->next=x->head;
          x->head=temp;
        }

      }
      break;
    }
    prev=temp;
    temp=temp->next;
  }
  
  return flg;
  
}


void insert_mru(struct mru* x,char* s,int count)
{
  
  if(x->head == NULL)
  {
    x->head=(struct node*)malloc(sizeof(struct node));
    x->tail=x->head;
    x->head->next=NULL;
    x->head->data=(char*)malloc(20*sizeof(char));//20 as word length
    strcpy(x->head->data, s);
    x->size=1;
    x->head->count=count;
    return;
  }
  
  struct node* temp=NULL;
  temp=(struct node*)malloc(sizeof(struct node));
  temp->next=x->head;
  x->head=temp;
  temp->count=count;
  temp->data=(char*)malloc(20*sizeof(char));//20 as word length
  strcpy(temp->data, s);
  if(x->size==10)
  {
    struct node* prev=NULL;
    temp=x->head;
    prev=temp;
    
    while(temp->next!=NULL)
    {
      prev=temp;
      temp=temp->next;
    }
    
    prev->next= NULL;
    
  }
  else
  {
    x->size=x->size + 1;
  }

return;
}


void creat_dict(struct dict* dict,char* s,int m)
{
  int n=dict->size,i,flg=0;

  for(i=0;i<n;i++)
  {
    if(strcmp(s,dict->list[i])==0)
    {
      flg=1;
      break;
    }
  }
  
  if(flg==0)
  {
    dict->list[n]=s;
    dict->size=dict->size+1;
  }
  
  return;
}


////// circular linked list part

void insert_mis()
{

return;
}

void display_mis()
{

return;
}

////// circular linked list part

int main()
{
  int i;
  FILE *fptr;
  char* data=(char*)malloc(100*sizeof(char));
  
  // making MRU
  struct mru* fmru=(struct mru*)malloc(sizeof(struct mru));
  fmru->size=0;
  fmru->head=NULL;
  fmru->tail=NULL;
  // making MRU
  
  // Making DICTIONARY
  struct dict* dict=(struct dict* )malloc(sizeof( struct dict));
  int dict_len=100,word_len=20;
  dict->size=0;
  dict->list=NULL;
  dict->list=(char**)malloc(dict_len*sizeof(char*));
  for(i=0;i<dict_len;i++)
  {
    dict->list[i]=(char*)malloc(word_len*sizeof(char));
  }
  // Making DICTIONARY


  fptr = fopen("\location of file","r"); // location of file goes here

  if(fptr == NULL)
  {
    printf("Error!");   
    exit(1);             
  }

  int idx=0;
  char outis;
  while(fgets(outis,1,fptr)!=NULL) 
  {
      
      if((outis>=65&&outis<=90)||(outis>=97&&outis<=122))
      {
        data[idx]=outis;
        idx++;
      }
      else if(idx>0)
      {
        data[idx]='\0';
        
        if(is_present(fmru,data,1,1)==1) // 1,1 TO increment the count and move it in front
        {
          
        }
        else
        {
          creat_dict(dict,data,idx+1);
          insert_mru(fmru,data,1);
          
        }
        idx=0;
      }
  }

  fclose(fptr);



  fptr = fopen("\location of file for spell check","r"); // file to check spell erros in

  if(fptr == NULL)
  {
    printf("Error!");   
    exit(1);             
  }

  int idx=0,flg;
  char outis;
  while(fgets(outis,1,fptr)!=NULL) 
  {
      
      if((outis>=65&&outis<=90)||(outis>=97&&outis<=122))
      {
        data[idx]=outis;
        idx++;
      }
      else if(idx>0)
      {
        data[idx]='\0';
        
        if(is_present(fmru,data,0,0)==1) // 1,1 TO increment the count and move it in front
        {
          // spelling is correct
        }
        else
        {
          flg=1;
          flg=search_dict(dict,data,idx+1);

          if(flg==0)
          {
            insert_mis();
          }
        }
        idx=0;
      }
  }

  display_mis();

  fclose(fptr);

  return 0;
}
