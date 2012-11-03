class CreateMessages < ActiveRecord::Migration
  def change
    create_table :messages do |t|
      t.string :sender
      t.string :subject
      t.string :to
      t.string :date
      t.text :body

      t.timestamps
    end
  end
end
