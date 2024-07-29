class PriorityQueue {
    constructor() {
        this.queue = [];
    }

    enqueue(element, priority) {
        this.queue.push({ element, priority });
        this.queue.sort((a, b) => a.priority - b.priority);
    }

    dequeue() {
        return this.queue.shift().element;
    }

    isEmpty() {
        return this.queue.length === 0;
    }
}

class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }

    addEdge(vertex1, vertex2, weight) {
        this.adjacencyList[vertex1].push({ node: vertex2, weight });
        this.adjacencyList[vertex2].push({ node: vertex1, weight }); // 무방향 그래프의 경우
    }

    dijkstra(start) {
        const distances = {};
        const priorityQueue = new PriorityQueue();
        const previous = {};

        // 초기 설정
        for (let vertex in this.adjacencyList) {
            if (vertex === start) {
                distances[vertex] = 0;
                priorityQueue.enqueue(vertex, 0);
            } else {
                distances[vertex] = Infinity;
                priorityQueue.enqueue(vertex, Infinity);
            }
            previous[vertex] = null;
        }

        while (!priorityQueue.isEmpty()) {
            const currentVertex = priorityQueue.dequeue();

            for (let neighbor of this.adjacencyList[currentVertex]) {
                const distance = distances[currentVertex] + neighbor.weight;

                if (distance < distances[neighbor.node]) {
                    distances[neighbor.node] = distance;
                    previous[neighbor.node] = currentVertex;
                    priorityQueue.enqueue(neighbor.node, distance);
                }
            }
        }

        return { distances, previous };
    }
}

// 사용 예시
const graph = new Graph();

graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addVertex('E');
graph.addVertex('F');

graph.addEdge('A', 'B', 4);
graph.addEdge('A', 'C', 2);
graph.addEdge('B', 'E', 3);
graph.addEdge('C', 'D', 2);
graph.addEdge('C', 'F', 4);
graph.addEdge('D', 'E', 3);
graph.addEdge('D', 'F', 1);
graph.addEdge('E', 'F', 1);

const result = graph.dijkstra('A');
console.log(result.distances); // A에서 각 정점까지의 최단 거리
console.log(result.previous);  // 최단 경로를 구하기 위한 이전 정점들