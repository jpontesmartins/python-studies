Studies with SQLAlchemy
===

O SQLAlchemy implementa esses três padrões do PoEAA:
- Data Mapper: https://martinfowler.com/eaaCatalog/dataMapper.html
- Identity Map: https://martinfowler.com/eaaCatalog/identityMap.html
- Unit of Work: https://martinfowler.com/eaaCatalog/unitOfWork.html

### Data Mapper

    "SQLAlchemy is most famous for its object-relational mapper (ORM), an optional component that provides the data mapper pattern, where classes can be mapped to the database in open ended, multiple ways - allowing the object model and database schema to develop in a cleanly decoupled way from the beginning."
	(https://www.sqlalchemy.org/)

### Identity Map
	"In SQLAlchemy, the Session object presents the public interface for the actual usage of the ORM—that is, loading and persisting data. It provides the starting point for queries and persistence operations for a given database connection.

	The Session, in addition to serving as the gateway for database connectivity, maintains an active reference to the set of all mapped entities which are present in memory relative to that Session. It's in this way that the Session implements a facade for the identity map and unit of work patterns, both identified by Fowler. The identity map maintains a database-identity-unique mapping of all objects for a particular Session, eliminating the problems introduced by duplicate identities. The unit of work builds on the identity map to provide a system of automating the process of persisting all changes in state to the database in the most effective manner possible. The actual persistence step is known as a "flush", and in modern SQLAlchemy this step is usually automatic."
	(http://aosabook.org/en/sqlalchemy.html#fig.sqlalchemy.session)
	(https://speakerdeck.com/zzzeek/the-sqlalchemy-session-in-depth?slide=26)

	The SQLAlchemy Session - In Depth
	https://speakerdeck.com/zzzeek/the-sqlalchemy-session-in-depth?slide=20

### Unit of Work
	"The flush method provided by Session turns over its work to a separate module called unitofwork. As mentioned earlier, the flush process is probably the most complex function of SQLAlchemy.

	The job of the unit of work is to move all of the pending state present in a particular Session out to the database, emptying out the new, dirty, and deleted collections maintained by the Session. "
	(http://aosabook.org/en/sqlalchemy.html#fig.sqlalchemy.toposort)