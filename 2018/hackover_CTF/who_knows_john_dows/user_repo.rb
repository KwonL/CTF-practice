class UserRepo

    def initialize(database)
      @database = database
      @users = database[:users]
    end
  
    def login(identification, password)
      hashed_input_password = hash(password)
      query = "select id, phone, email from users where email = '#{identification}' and password_digest = '#{hashed_input_password}' limit 1"
      puts "SQL executing: '#{query}'"
      @database[query].first if user_exists?(identification)
    end
  
    def user_exists?(identification)
      !get_user_by_identification(identification).nil?
    end
  
    private
  
    def get_user_by_identification(identification)
      @users.where(phone: identification).or(email: identification).first
    end
  
    def hash(password)
      password.reverse
    end
  
  end