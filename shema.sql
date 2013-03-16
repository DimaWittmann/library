create table book(
	book_id integer primary key autoincrement,
	title text not null
);

create table author(
	author_id integer primary key autoincrement,
	authorname text not null
);

create table book_author(
	book_id integer not null,
	author_id integer not null,
	primary key(book_id, author_id)
);

create table user (
  user_id integer primary key autoincrement,
  username text not null,
  email text not null,
  pw_hash text not null,
  usertype integer not null
);