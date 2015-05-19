/* DBの設計 */
/*
	initDB.pyを実行した際に,
	本ファイルで定義したDBが作成される。
*/
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);