class Person:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def __repr__(self):
        return self.name

    def add_connection(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)


idris = Person("Idris")
kamil = Person("Kamil")
lina = Person("Lina")
sasha = Person("Sasha")
talia = Person("Talia")
ken = Person("Ken")
marco = Person("Marco")

idris.add_connection(kamil)
kamil.add_connection(idris)

idris.add_connection(talia)
talia.add_connection(idris)

kamil.add_connection(lina)
lina.add_connection(kamil)

talia.add_connection(ken)
ken.add_connection(talia)

ken.add_connection(marco)
marco.add_connection(ken)

marco.add_connection(sasha)
sasha.add_connection(marco)

sasha.add_connection(lina)
lina.add_connection(sasha)


def find_degrees_of_separation(p1, p2):
    lowest_degrees_of_separation = {}
    nearest_mutual_friend = {}

    unvisited_people = [p1]

    visited_people = {}
    visited_people[p1.name] = True

    lowest_degrees_of_separation[p1.name] = 0

    while len(unvisited_people) > 0:
        current_person = unvisited_people.pop(0)
        visited_people[current_person.name] = True

        for connection in current_person.connections:
            if not visited_people.get(connection.name, False) and connection not in unvisited_people:
                unvisited_people.append(connection)

                # Calculate degrees of separation via current person
                dos_through_current_person = lowest_degrees_of_separation[current_person.name] + 1

                # If it's a quicker route, update
                if not lowest_degrees_of_separation.get(connection.name, False) or dos_through_current_person < lowest_degrees_of_separation.get(connection.name, 0):
                    lowest_degrees_of_separation[connection.name] = dos_through_current_person
                    nearest_mutual_friend[connection.name] = current_person.name

    shortest_path = []
    current_person_name = p2.name

    while current_person_name != p1.name:
        shortest_path.append(current_person_name)
        current_person_name = nearest_mutual_friend[current_person_name]

    shortest_path.append(p1.name)
    shortest_path.reverse()

    return shortest_path


print(find_degrees_of_separation(idris, marco))
