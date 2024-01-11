graph={
    '1':['2'],
    '2':['1','3'],
    '3':['2','4'],
    '4':['3','5','24'],
    '5':['4','6'],
    '6':['5','7'],
    '7':['6','27'],
    '8':['9'],
    '9':['8','10'],
    '10':['9','30','11'],
    '11':['10','12'],
    '12':['11','32'],
    '13':['14'],
    '14':['13','15'],
    '15':['14','16'],
    '16':['15','17'],
    '17':['16','37'],
    '18':['19','38'],
    '19':['18','20','39'],
    '20':['19'],





    '21':['22','41'],
    '22':['21','23'],
    '23':['22','24'],
    '24':['23','4'],
    '25':['26'],
    '26':['25','46'],
    '27':['7','28'],
    '28':['27','48'],
    '29':['30','49'],
    '30':['10','29'],
    '31':['51'],
    '32':['12','33'],
    '33':['32','34'],
    '34':['33','54'],
    '35':['36','55'],
    '36':['35','37'],
    '37':['17','36'],
    '38':['18','58'],
    '39':['19','40'],
    '40':['39','60'],



    '41':['21','42'],
    '42':['41','43'],
    '43':['42','63'],
    '44':['45'],
    '45':['44','65','46'],
    '46':['26','45','47'],
    '47':['46'],
    '48':['28','49'],
    '49':['29','48'],
    '50':['51','70'],
    '51':['50','31','52'],
    '52':['51','53'],
    '53':['52','54'],
    '54':['34','53','74'],
    '55':['35','56'],
    '56':['55','57'],
    '57':['56','58'],
    '58':['38','57','59'],
    '59':['58'],
    '60':['40','80'],





    '61':['81','62'],
    '62':['61','82'],
    '63':['43','64'],
    '64':['63','84'],
    '65':['45','66'],
    '66':['65','67'],
    '67':['66','68'],
    '68':['67','69'],
    '69':['89','68'],
    '70':['50','90'],
    '71':['72','91'],
    '72':['71','73'],
    '73':['72','93'],
    '74':['54','75'],
    '75':['74','76'],
    '76':['75','77'],
    '77':['76','78'],
    '78':['77','79','98'],
    '79':['78','80'],
    '80':['60','79'],





    '81':['61','101'],
    '82':['62','83'],
    '83':['82','84'],
    '84':['64','83'],
    '85':['86','105'],
    '86':['85','106'],
    '87':['107','88'],
    '88':['87','108'],
    '89':['69','109'],
    '90':['70','110'],
    '91':['71','111'],
    '92':['93','112'],
    '93':['92','73','113'],
    '94':['95','114'],
    '95':['94','115'],
    '96':['116','97'],
    '97':['96','98'],
    '98':['97','78','118'],
    '99':['100','119'],
    '100':['120','99'],







    '101':['81','121'],
    '102':['103','122'],
    '103':['102','104'],
    '104':['103','124'],
    '105':['85','125'],
    '106':['86','107'],
    '107':['87','106'],
    '108':['88','128'],
    '109':['89','110'],
    '110':['90','109'],
    '111':['91','131'],
    '112':['92','132'],
    '113':['93','114'],
    '114':['94','113'],
    '115':['95','135'],
    '116':['96','117'],
    '117':['116'],
    '118':['98','138','119'],
    '119':['118','99'],
    '120':['140','100'],





    '121':['101'],
    '122':['123','102'],
    '123':['122'],
    '124':['104','125'],
    '125':['105','124'],
    '126':['127'],
    '127':['128','126'],
    '128':['108','127','129'],
    '129':['128','130'],
    '130':['129','131'],
    '131':['130','111'],
    '132':['112','133'],
    '133':['132','134'],
    '134':['133'],
    '135':['115','136'],
    '136':['135','137'],
    '137':['136','138'],
    '138':['118','137','139'],
    '139':['138','140'],
    '140':['139','120'],

}
def bfs(graph):
    #https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/ Took inspiration from this website
    from queue import Queue
    visited_nodes={}
    parent_node={}
    queue_bfs = Queue()
    for every_node in graph.keys():
        visited_nodes[every_node]=False#initially no node is visited so it is set to false
        parent_node[every_node]=None#initially no node has a parent
    source_node='1' #defining the source node
    visited_nodes[source_node]=True
    queue_bfs.put(source_node)
    while not queue_bfs.empty():#While the queue is not empty
        popped_element=queue_bfs.get()#queue.get() removes and returns a node from the queue
        for elements in graph[popped_element]:#for all the nodes just removed from the queue
            if not visited_nodes[elements]:#This makes sure the nodes that are already visited are not visited again
                visited_nodes[elements]=True#Visting neighbours of all the nodes that are just removed from the queue
                parent_node[elements]=popped_element#This is used to find the path
                queue_bfs.put(elements)#adding the neighbours to the queue
    destination_node='139'
    path_list=[]
    while destination_node is not None:#The parent of the source node is none
        path_list.append(destination_node)#appending the destination node
        destination_node=parent_node[destination_node]
    for i in range (0,len(path_list)):
        print(path_list[i],end='->')#Prints the path if it exists from destination to source using bfs
def dfs(graph):
    #https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/ Took inspiration from this website
    source_node="1"#Change this if the source node changes
    List_traverse=[]
    stack=[]
    parent_node={}
    visited_nodes={}
    for every_node in graph.keys():
        visited_nodes[every_node]=False#initially no node is visited so it is set to false
        parent_node[every_node]=None#initially no node has a parent
    visited_nodes[source_node]=True
    parent_node[source_node]=None
    #first put the source_node into the stack
    stack.append(source_node)
    while stack:
        popped_node=stack.pop()#removes the node from the stack
        if popped_node not in List_traverse:#This is for the dfs search, appending the popped nodes to the dfs search
            List_traverse.append(popped_node)
        elif popped_node in List_traverse:#Dont append if it already exists
            continue
        for elements in graph[popped_node]:#for all the popped elements from the stack
            if not visited_nodes[elements]:#If the neighbours are not visited
                visited_nodes[elements]=True#Visiting all the neighbours of the popped element
                parent_node[elements]=popped_node#This is for the path from source to destination/destination->source
                stack.append(elements)#adding the neighbours to the stack
    #print(List_traverse) #print this to see the dfs search
    #print ("printing path now \n\n\n")
    destination_node='139'#Destination node, see image represenation of maze
    path_list=[]
    while destination_node is not None:#the parent of the source node is none
        path_list.append(destination_node)#Tracing the path from the destination to the source, this is why parent_node is used in the above for loop
        destination_node=parent_node[destination_node]
    for i in range (0,len(path_list)):
        print(path_list[i],end='->')


#Code to check which type of search the user entered
type_of_search=input("Input the type of search (bfs or dfs?)")
if (type_of_search=="bfs" or type_of_search=="BFS"):
    bfs(graph)
elif (type_of_search=="dfs" or type_of_search=="DFS"):
    dfs(graph)
else:
    print("Type of search not available")

#Comment out this code to not see the graph representation
#https://networkx.org/documentation/stable/reference/drawing.html This was used for visualizing the graph
import networkx
import matplotlib.pyplot
network_graph=networkx.Graph()
network_graph.add_nodes_from(graph.keys())#This is to visualise the graph, adding nodes to networkx
for keys,values in graph.items():
    network_graph.add_edges_from (([(keys, t) for t in values]))#adding edges to networkx #Note networkx visualizes the graph differently each time you run it
pos=networkx.spring_layout(network_graph,scale=1)
networkx.draw(network_graph,pos,with_labels=True,width=1,node_size=5,font_size=9)
matplotlib.pyplot.draw()
matplotlib.pyplot.show()

